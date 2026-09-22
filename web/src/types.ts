export type ProviderShare = {
  provider: string
  value: number
  unit: string
}

export type MarketSection = {
  service_name: string
  period: string
  geography: string
  total_accesses: number
  accesses_5g?: number | null
  share_5g_pct?: number | null
  fiber_accesses?: number | null
  provider_market_share: ProviderShare[]
  ranking_complete: boolean
}

export type SatisfactionRow = {
  service: string
  provider: string
  isg: number
}

export type PublicSource = {
  source_id: string
  service: string
  kind: string
  frequency: string
  landing_url: string
  format?: string
  glossary_url?: string
}

export type DashboardContractV2 = {
  contract_version: '2.0'
  data_mode: 'official_public'
  authority: string
  market: {
    SMP: MarketSection
    SCM: MarketSection
  }
  satisfaction: {
    year: number
    rows: SatisfactionRow[]
  }
  sources: PublicSource[]
  methodology_notes: string[]
}
