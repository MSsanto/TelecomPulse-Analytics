import { cleanup, render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { afterEach, describe, expect, it, vi } from 'vitest'
import App from './App'
import { dashboardFixture } from './test/fixture'

function mockFetchOk(payload = dashboardFixture) {
  vi.stubGlobal(
    'fetch',
    vi.fn().mockResolvedValue({
      ok: true,
      json: vi.fn().mockResolvedValue(payload),
    }),
  )
}

afterEach(() => {
  cleanup()
  vi.unstubAllGlobals()
})

describe('TelecomPulse v2 public dashboard', () => {
  it('renders official public data instead of synthetic NOC metrics', async () => {
    mockFetchOk()
    render(<App />)

    expect(screen.getByText(/Carregando dados oficiais/i)).toBeInTheDocument()
    expect(await screen.findByRole('heading', { name: /TelecomPulse/i })).toBeInTheDocument()
    expect(screen.getByText('Dados públicos oficiais')).toBeInTheDocument()
    expect(screen.getByText('37,9%')).toBeInTheDocument()
    expect(screen.queryByText(/MTTR/i)).not.toBeInTheDocument()
    expect(screen.queryByText(/Downtime/i)).not.toBeInTheDocument()
  })

  it('switches satisfaction service without changing market facts', async () => {
    mockFetchOk()
    const user = userEvent.setup()
    render(<App />)

    await screen.findByText('Brisanet')
    await user.selectOptions(
      screen.getByLabelText('Serviço da pesquisa de satisfação'),
      'celular_pos_pago',
    )

    expect(screen.queryByText('Brisanet')).not.toBeInTheDocument()
    expect(screen.getAllByText('Vivo').length).toBeGreaterThan(0)
    expect(screen.getByText('37,9%')).toBeInTheDocument()
  })

  it('renders a useful HTTP error state', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: false, status: 500 }))
    render(<App />)

    expect(
      await screen.findByRole('heading', { name: /não foi possível carregar os dados públicos/i }),
    ).toBeInTheDocument()
    expect(screen.getByRole('alert')).toHaveTextContent('HTTP 500')
  })

  it('rejects a synthetic or incompatible contract', async () => {
    mockFetchOk({ ...dashboardFixture, data_mode: 'synthetic' as 'official_public' })
    render(<App />)

    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Contrato público incompatível')
    })
  })
})
