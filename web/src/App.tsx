import { useEffect, useMemo, useState } from 'react'
import type { DashboardContract, Incident, MetricRow, TimelineRow } from './types'

type Filters = {
  carrier: string
  site: string
  cause: string
  status: string
}

const EMPTY_FILTERS: Filters = {
  carrier: 'all',
  site: 'all',
  cause: 'all',
  status: 'all',
}

function formatNumber(value: number, maximumFractionDigits = 0) {
  return new Intl.NumberFormat('pt-BR', { maximumFractionDigits }).format(value)
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat('pt-BR', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
    timeZone: 'UTC',
  }).format(new Date(value))
}

function formatDateTime(value: string | null) {
  if (!value) return 'Em aberto'
  return new Intl.DateTimeFormat('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'UTC',
  }).format(new Date(value))
}

function humanize(value: string) {
  return value.replaceAll('_', ' ').replace(/\b\w/g, (letter) => letter.toUpperCase())
}

function KpiCard({
  label,
  value,
  hint,
}: {
  label: string
  value: string
  hint: string
}) {
  return (
    <article className="kpi-card">
      <span className="kpi-label">{label}</span>
      <strong className="kpi-value">{value}</strong>
      <span className="kpi-hint">{hint}</span>
    </article>
  )
}

function Ranking({
  id,
  title,
  subtitle,
  rows,
}: {
  id: string
  title: string
  subtitle: string
  rows: Array<MetricRow & { label: string }>
}) {
  const sorted = [...rows].sort((a, b) => b.downtime_minutes - a.downtime_minutes)
  const max = Math.max(...sorted.map((row) => row.downtime_minutes), 1)

  return (
    <section className="panel" aria-labelledby={`ranking-${id}`}>
      <div className="section-heading">
        <div>
          <p className="section-kicker">Concentração operacional</p>
          <h2 id={`ranking-${id}`}>{title}</h2>
        </div>
        <p>{subtitle}</p>
      </div>
      <div className="ranking-list">
        {sorted.map((row) => {
          return (
            <article className="ranking-row" key={row.label}>
              <div className="ranking-copy">
                <strong>{row.label}</strong>
                <span>
                  {formatNumber(row.incident_count)} incidentes · {formatNumber(row.downtime_minutes)} min
                </span>
              </div>
              <div className="bar-track" aria-hidden="true">
                <span
                  className="bar-fill"
                  style={{ width: `${Math.max((row.downtime_minutes / max) * 100, 3)}%` }}
                />
              </div>
              <span className="ranking-availability">
                {formatNumber(row.availability_pct, 2)}%
              </span>
            </article>
          )
        })}
      </div>
    </section>
  )
}

function Timeline({ rows }: { rows: TimelineRow[] }) {
  const max = Math.max(...rows.map((row) => row.downtime_minutes), 1)

  return (
    <section className="panel timeline-panel" aria-labelledby="timeline-title">
      <div className="section-heading">
        <div>
          <p className="section-kicker">Evolução temporal</p>
          <h2 id="timeline-title">Downtime por data de abertura</h2>
        </div>
        <p>Coorte UTC: o downtime fica associado ao dia em que o incidente foi aberto.</p>
      </div>
      <div className="timeline" role="list">
        {rows.map((row) => (
          <div className="timeline-item" role="listitem" key={row.opened_date}>
            <div className="timeline-meta">
              <strong>{formatDate(row.opened_date)}</strong>
              <span>{row.incident_count} incidente(s)</span>
            </div>
            <div className="timeline-track" aria-hidden="true">
              <span
                style={{ height: `${Math.max((row.downtime_minutes / max) * 100, 6)}%` }}
              />
            </div>
            <span className="timeline-value">{formatNumber(row.downtime_minutes)} min</span>
          </div>
        ))}
      </div>
    </section>
  )
}

function IncidentTable({
  incidents,
  total,
}: {
  incidents: Incident[]
  total: number
}) {
  return (
    <section className="panel" aria-labelledby="incidents-title">
      <div className="section-heading">
        <div>
          <p className="section-kicker">Detalhe filtrável</p>
          <h2 id="incidents-title">Incidentes</h2>
        </div>
        <p>
          Exibindo <strong>{incidents.length}</strong> de {total}. Os filtros não recalculam os KPIs executivos.
        </p>
      </div>
      {incidents.length === 0 ? (
        <div className="empty-inline">
          <strong>Nenhum incidente encontrado.</strong>
          <span>Altere ou limpe os filtros para recuperar registros.</span>
        </div>
      ) : (
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Incidente</th>
                <th>Unidade</th>
                <th>Operadora</th>
                <th>Status</th>
                <th>Causa</th>
                <th>Abertura</th>
                <th>Restauração</th>
                <th>Downtime</th>
              </tr>
            </thead>
            <tbody>
              {incidents.map((incident) => (
                <tr key={incident.incident_id}>
                  <td className="mono">{incident.incident_id}</td>
                  <td>{incident.site_id}</td>
                  <td>{incident.carrier}</td>
                  <td>
                    <span className={`status status-${incident.status}`}>
                      {incident.status === 'resolved' ? 'Resolvido' : 'Em aberto'}
                    </span>
                  </td>
                  <td>{humanize(incident.cause_category)}</td>
                  <td>{formatDateTime(incident.opened_at)}</td>
                  <td>{formatDateTime(incident.restored_at)}</td>
                  <td>
                    {incident.downtime_minutes === null
                      ? '—'
                      : `${formatNumber(incident.downtime_minutes)} min`}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  )
}

function Dashboard({ data }: { data: DashboardContract }) {
  const [filters, setFilters] = useState<Filters>(EMPTY_FILTERS)

  const options = useMemo(
    () => ({
      carriers: [...new Set(data.incidents.map((incident) => incident.carrier))].sort(),
      sites: [...new Set(data.incidents.map((incident) => incident.site_id))].sort(),
      causes: [...new Set(data.incidents.map((incident) => incident.cause_category))].sort(),
    }),
    [data.incidents],
  )

  const filteredIncidents = useMemo(
    () =>
      data.incidents.filter(
        (incident) =>
          (filters.carrier === 'all' || incident.carrier === filters.carrier) &&
          (filters.site === 'all' || incident.site_id === filters.site) &&
          (filters.cause === 'all' || incident.cause_category === filters.cause) &&
          (filters.status === 'all' || incident.status === filters.status),
      ),
    [data.incidents, filters],
  )

  const updateFilter = (key: keyof Filters, value: string) => {
    setFilters((current) => ({ ...current, [key]: value }))
  }

  const summary = data.summary

  return (
    <main className="app-shell">
      <header className="hero">
        <div>
          <p className="eyebrow">TELECOM OPERATIONS INTELLIGENCE</p>
          <h1>TelecomPulse <span>Analytics</span></h1>
          <p className="hero-copy">
            Disponibilidade, downtime e recorrência transformados em uma leitura operacional única.
          </p>
        </div>
        <div className="hero-meta" aria-label="Contexto do dataset">
          <span className="dataset-badge">Dataset sintético</span>
          <dl>
            <div>
              <dt>Contrato</dt>
              <dd>v{data.contract_version}</dd>
            </div>
            <div>
              <dt>Janela</dt>
              <dd>{formatDate(data.window.start)} — {formatDate(data.window.end)}</dd>
            </div>
            <div>
              <dt>Fonte</dt>
              <dd>{data.generated_from}</dd>
            </div>
          </dl>
        </div>
      </header>

      <section className="kpi-grid" aria-label="Indicadores executivos">
        <KpiCard
          label="Disponibilidade"
          value={`${formatNumber(summary.availability_pct, 2)}%`}
          hint="Site-time, sem dupla contagem"
        />
        <KpiCard
          label="Downtime bruto"
          value={`${formatNumber(summary.downtime_minutes)} min`}
          hint="Soma dos incidentes resolvidos"
        />
        <KpiCard
          label="MTTR"
          value={`${formatNumber(summary.mttr_minutes)} min`}
          hint="Tempo médio de restauração"
        />
        <KpiCard
          label="Incidentes"
          value={formatNumber(summary.incident_count)}
          hint={`${summary.open_incident_count} aberto(s) · ${summary.resolved_incident_count} resolvido(s)`}
        />
        <KpiCard
          label="Recorrências"
          value={formatNumber(summary.recurrence_count)}
          hint="Ocorrências além da primeira por site"
        />
        <KpiCard
          label="Unidades"
          value={formatNumber(summary.site_count)}
          hint="Sites presentes na janela"
        />
      </section>

      <Timeline rows={data.timeline} />

      <div className="ranking-grid">
        <Ranking
          id="carrier"
          title="Operadoras"
          subtitle="Ordenadas por downtime bruto."
          rows={data.by_carrier.map((row) => ({ ...row, label: row.carrier }))}
        />
        <Ranking
          id="site"
          title="Unidades"
          subtitle="Onde a indisponibilidade se concentrou."
          rows={data.by_site.map((row) => ({ ...row, label: row.site_id }))}
        />
        <Ranking
          id="cause"
          title="Causas"
          subtitle="Categorias de maior impacto."
          rows={data.by_cause.map((row) => ({ ...row, label: humanize(row.cause_category) }))}
        />
      </div>

      <section className="panel filters-panel" aria-labelledby="filters-title">
        <div className="section-heading">
          <div>
            <p className="section-kicker">Investigação</p>
            <h2 id="filters-title">Filtrar detalhe</h2>
          </div>
          <button
            className="text-button"
            type="button"
            onClick={() => setFilters(EMPTY_FILTERS)}
            disabled={Object.values(filters).every((value) => value === 'all')}
          >
            Limpar filtros
          </button>
        </div>
        <div className="filters-grid">
          <label>
            <span>Operadora</span>
            <select value={filters.carrier} onChange={(event) => updateFilter('carrier', event.target.value)}>
              <option value="all">Todas</option>
              {options.carriers.map((carrier) => <option key={carrier}>{carrier}</option>)}
            </select>
          </label>
          <label>
            <span>Unidade</span>
            <select value={filters.site} onChange={(event) => updateFilter('site', event.target.value)}>
              <option value="all">Todas</option>
              {options.sites.map((site) => <option key={site}>{site}</option>)}
            </select>
          </label>
          <label>
            <span>Causa</span>
            <select value={filters.cause} onChange={(event) => updateFilter('cause', event.target.value)}>
              <option value="all">Todas</option>
              {options.causes.map((cause) => <option key={cause} value={cause}>{humanize(cause)}</option>)}
            </select>
          </label>
          <label>
            <span>Status</span>
            <select value={filters.status} onChange={(event) => updateFilter('status', event.target.value)}>
              <option value="all">Todos</option>
              <option value="resolved">Resolvido</option>
              <option value="open">Em aberto</option>
            </select>
          </label>
        </div>
        <p className="filter-note">
          Os filtros alteram apenas a tabela. KPIs e rankings permanecem nos agregados homologados do contrato v1.
        </p>
      </section>

      <IncidentTable incidents={filteredIncidents} total={data.incidents.length} />

      <footer>
        <strong>TelecomPulse Analytics</strong>
        <span>Dados sintéticos · métricas definidas em docs/METRICS.md</span>
      </footer>
    </main>
  )
}

export default function App() {
  const [data, setData] = useState<DashboardContract | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let active = true
    fetch('/data/dashboard-v1.json')
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`)
        return response.json()
      })
      .then((payload: DashboardContract) => {
        if (!active) return
        if (payload.contract_version !== '1.0') {
          throw new Error('Contrato incompatível')
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
        <h1>Não foi possível carregar o contrato analítico.</h1>
        <p>{error}</p>
        <p>Confirme a geração de <code>web/public/data/dashboard-v1.json</code>.</p>
      </main>
    )
  }

  if (!data) {
    return (
      <main className="state-shell" aria-live="polite">
        <span className="loader" aria-hidden="true" />
        <h1>Carregando dados operacionais…</h1>
        <p>Validando o contrato dashboard v1.</p>
      </main>
    )
  }

  if (data.incidents.length === 0) {
    return (
      <main className="state-shell">
        <span className="state-code">EMPTY_DATASET</span>
        <h1>O contrato é válido, mas não há incidentes para exibir.</h1>
        <p>Gere o dataset analítico novamente ou revise a janela de análise.</p>
      </main>
    )
  }

  return <Dashboard data={data} />
}
