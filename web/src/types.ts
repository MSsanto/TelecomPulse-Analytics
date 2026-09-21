export type MetricRow = {
  incident_count: number
  resolved_incident_count: number
  open_incident_count: number
  downtime_minutes: number
  mttr_minutes: number
  recurrence_count: number
  availability_pct: number
  site_count: number
}

export type CarrierMetric = MetricRow & { carrier: string }
export type SiteMetric = MetricRow & { site_id: string }
export type CauseMetric = MetricRow & { cause_category: string }

export type TimelineRow = {
  opened_date: string
  incident_count: number
  resolved_incident_count: number
  open_incident_count: number
  downtime_minutes: number
}

export type Incident = {
  incident_id: string
  site_id: string
  carrier: string
  opened_at: string
  restored_at: string | null
  status: 'open' | 'resolved'
  cause_category: string
  region: string
  link_type: string
  source: string
  downtime_minutes: number | null
}

export type DashboardContract = {
  contract_version: '1.0'
  generated_from: string
  window: {
    start: string
    end: string
  }
  summary: MetricRow
  by_carrier: CarrierMetric[]
  by_site: SiteMetric[]
  by_cause: CauseMetric[]
  timeline: TimelineRow[]
  incidents: Incident[]
}
