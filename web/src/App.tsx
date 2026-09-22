import { useEffect, useMemo, useState } from 'react'
import type { DashboardContractV2, MarketSection, SatisfactionRow } from './types'

function number(value: number, maximumFractionDigits = 1) {
  return new Intl.NumberFormat('pt-BR', { maximumFractionDigits }).format(value)
}

function compact(value: number) {
  return new Intl.NumberFormat('pt-BR', {
    notation: 'compact',
    maximumFractionDigits: 1,
  }).format(value)
}

function serviceLabel(service: string) {
  const labels: Record<string, string> = {
    internet_fixa: 'Internet fixa',
    celular_pos_pago: 'Celular pós-pago',
    celular_pre_pago: 'Celular pré-pago',
  }
  return labels[service] ?? service.replaceAll('_', ' ')
}

function Kpi({ label, value, hint }: { label: string; value: string; hint: string }) {
  return (
    <article className="kpi-card">
      <span className="kpi-label">{label}</span>
      <strong className="kpi-value">{value}</strong>
      <span className="kpi-hint">{hint}</span>
    </article>
  )
}

function MarketShare({ market }: { market: MarketSection }) {
  const max = Math.max(...market.provider_market_share.map((row) => row.value), 1)

  return (
    <section className="panel" aria-labelledby={`market-${market.service_name}`}>
      <div className="section-heading">
        <div>
          <p className="section-kicker">{market.period} · Brasil</p>
          <h2 id={`market-${market.service_name}`}>{market.service_name}</h2>
        </div>
        <p>
          Participação publicada no snapshot oficial.
          {!market.ranking_complete && ' Ranking parcial até a ingestão mensal completa.'}
        </p>
      </div>
      <div className="ranking-list">
        {market.provider_market_share.map((row) => (
          <article className="ranking-row" key={row.provider}>
            <div className="ranking-copy">
              <strong>{row.provider}</strong>
              <span>participação de mercado</span>
            </div>
            <div className="bar-track" aria-hidden="true">
              <span className="bar-fill" style={{ width: `${(row.value / max) * 100}%` }} />
            </div>
            <span className="ranking-availability">{number(row.value)}%</span>
          </article>
        ))}
      </div>
    </section>
  )
}

function Satisfaction({ rows, year }: { rows: SatisfactionRow[]; year: number }) {
  const services = [...new Set(rows.map((row) => row.service))]
  const [service, setService] = useState(services[0] ?? '')
  const selected = useMemo(
    () => rows.filter((row) => row.service === service).sort((a, b) => b.isg - a.isg),
    [rows, service],
  )

  return (
    <section className="panel" aria-labelledby="satisfaction-title">
      <div className="section-heading">
        <div>
          <p className="section-kicker">Pesquisa Anatel {year}</p>
          <h2 id="satisfaction-title">Satisfação geral</h2>
        </div>
        <label>
          <span className="sr-only">Serviço da pesquisa de satisfação</span>
          <select value={service} onChange={(event) => setService(event.target.value)}>
            {services.map((item) => (
              <option key={item} value={item}>{serviceLabel(item)}</option>
            ))}
          </select>
        </label>
      </div>
      <div className="table-wrap" tabIndex={0}>
        <table>
          <caption className="sr-only">Índice de Satisfação Geral por prestadora e serviço.</caption>
          <thead>
            <tr>
              <th>Prestadora</th>
              <th>Serviço</th>
              <th>ISG</th>
            </tr>
          </thead>
          <tbody>
            {selected.map((row) => (
              <tr key={`${row.service}-${row.provider}`}>
                <td><strong>{row.provider}</strong></td>
                <td>{serviceLabel(row.service)}</td>
                <td>{number(row.isg, 2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  )
}

function Dashboard({ data }: { data: DashboardContractV2 }) {
  const mobile = data.market.SMP
  const fixed = data.market.SCM

  return (
    <main className="app-shell" id="dashboard-main">
      <a className="skip-link" href="#executive-summary">Pular para indicadores</a>

      <header className="hero">
        <div>
          <p className="eyebrow">BRAZILIAN TELECOM MARKET & QUALITY INTELLIGENCE</p>
          <h1>TelecomPulse <span>Analytics</span></h1>
          <p className="hero-copy">
            Mercado e experiência das telecomunicações brasileiras a partir de dados públicos oficiais.
          </p>
        </div>
        <div className="hero-meta" aria-label="Contexto dos dados">
          <span className="dataset-badge">Dados públicos oficiais</span>
          <dl>
            <div><dt>Autoridade</dt><dd>{data.authority}</dd></div>
            <div><dt>Contrato</dt><dd>v{data.contract_version}</dd></div>
            <div><dt>Modo</dt><dd>Real / public data</dd></div>
          </dl>
        </div>
      </header>

      <section className="kpi-grid" id="executive-summary" aria-label="Panorama de mercado" tabIndex={-1}>
        <Kpi label="Acessos móveis" value={compact(mobile.total_accesses)} hint={`SMP · ${mobile.period}`} />
        <Kpi label="Acessos 5G" value={compact(mobile.accesses_5g ?? 0)} hint="Base móvel 5G" />
        <Kpi label="Participação 5G" value={`${number(mobile.share_5g_pct ?? 0)}%`} hint="Sobre acessos móveis" />
        <Kpi label="Banda larga fixa" value={compact(fixed.total_accesses)} hint={`SCM · ${fixed.period}`} />
        <Kpi label="Acessos em fibra" value={compact(fixed.fiber_accesses ?? 0)} hint="Base fixa em fibra óptica" />
      </section>

      <div className="market-grid">
        <MarketShare market={mobile} />
        <MarketShare market={fixed} />
      </div>

      <Satisfaction rows={data.satisfaction.rows} year={data.satisfaction.year} />

      <section className="panel" aria-labelledby="methodology-title">
        <div className="section-heading">
          <div>
            <p className="section-kicker">Transparência</p>
            <h2 id="methodology-title">Metodologia e fontes</h2>
          </div>
          <p>O dashboard não completa valores ausentes por estimativa silenciosa.</p>
        </div>

        <div className="source-grid">
          {data.sources.map((source) => (
            <article className="source-card" key={source.source_id}>
              <span className="section-kicker">{source.kind}</span>
              <strong>{source.source_id}</strong>
              <span>{source.frequency}</span>
              <a href={source.landing_url} target="_blank" rel="noreferrer">Abrir fonte oficial</a>
            </article>
          ))}
        </div>

        <ul className="methodology-list">
          {data.methodology_notes.map((note) => <li key={note}>{note}</li>)}
        </ul>
      </section>

      <footer>
        <strong>TelecomPulse Analytics v2</strong>
        <span>Fonte primária: Agência Nacional de Telecomunicações — Anatel</span>
      </footer>
    </main>
  )
}

export default function App() {
  const [data, setData] = useState<DashboardContractV2 | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let active = true
    fetch('/data/dashboard-v2.json')
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`)
        return response.json()
      })
      .then((payload: DashboardContractV2) => {
        if (!active) return
        if (payload.contract_version !== '2.0' || payload.data_mode !== 'official_public') {
          throw new Error('Contrato público incompatível')
        }
        setData(payload)
      })
      .catch((reason: unknown) => {
        if (active) setError(reason instanceof Error ? reason.message : 'Falha desconhecida')
      })

    return () => {
      active = false
    }
  }, [])

  if (error) {
    return (
      <main className="state-shell" role="alert">
        <span className="state-code">DATA_ERROR</span>
        <h1>Não foi possível carregar os dados públicos.</h1>
        <p>{error}</p>
        <button className="retry-button" type="button" onClick={() => window.location.reload()}>
          Tentar novamente
        </button>
      </main>
    )
  }

  if (!data) {
    return (
      <main className="state-shell" aria-live="polite">
        <span className="loader" aria-hidden="true" />
        <h1>Carregando dados oficiais…</h1>
        <p>Validando o contrato público v2.</p>
      </main>
    )
  }

  return <Dashboard data={data} />
}
