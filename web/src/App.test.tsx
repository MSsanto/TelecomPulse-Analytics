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

describe('TelecomPulse dashboard', () => {
  it('renders loading then the governed dashboard contract', async () => {
    mockFetchOk()
    render(<App />)

    expect(screen.getByText(/Carregando dados operacionais/i)).toBeInTheDocument()
    expect(await screen.findByRole('heading', { name: /TelecomPulse/i })).toBeInTheDocument()
    expect(screen.getByText('Dataset sintético')).toBeInTheDocument()
    expect(screen.getByText('99,5%')).toBeInTheDocument()
    expect(screen.getByText('INC-0001')).toBeInTheDocument()
  })

  it('filters incident detail without replacing executive KPI content', async () => {
    mockFetchOk()
    const user = userEvent.setup()
    render(<App />)

    await screen.findByText('INC-0001')
    await user.selectOptions(screen.getByLabelText('Operadora'), 'Carrier B')

    expect(screen.queryByText('INC-0001')).not.toBeInTheDocument()
    expect(screen.getByText('INC-0002')).toBeInTheDocument()
    expect(screen.getByText('99,5%')).toBeInTheDocument()
    expect(screen.getByText(/Exibindo/i)).toHaveTextContent('1 de 2')
  })

  it('renders the empty contract state', async () => {
    mockFetchOk({ ...dashboardFixture, incidents: [] })
    render(<App />)

    expect(
      await screen.findByRole('heading', { name: /não há incidentes para exibir/i }),
    ).toBeInTheDocument()
  })

  it('renders a useful error state when contract loading fails', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn().mockResolvedValue({
        ok: false,
        status: 500,
      }),
    )
    render(<App />)

    expect(
      await screen.findByRole('heading', { name: /não foi possível carregar/i }),
    ).toBeInTheDocument()
    expect(screen.getByRole('alert')).toHaveTextContent('HTTP 500')
  })

  it('rejects an incompatible contract version', async () => {
    mockFetchOk({ ...dashboardFixture, contract_version: '2.0' as '1.0' })
    render(<App />)

    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Contrato incompatível')
    })
  })
})
