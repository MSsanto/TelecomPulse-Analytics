import type { DashboardContractV2 } from '../types'

export const dashboardFixture: DashboardContractV2 = {
  contract_version: '2.0',
  data_mode: 'official_public',
  authority: 'Agência Nacional de Telecomunicações - Anatel',
  market: {
    SMP: {
      service_name: 'Telefonia móvel',
      period: '2026-Q2',
      geography: 'BR',
      total_accesses: 276400000,
      accesses_5g: 66100000,
      share_5g_pct: 23.9,
      provider_market_share: [
        { provider: 'Vivo', value: 37.9, unit: 'percent' },
        { provider: 'TIM', value: 22.4, unit: 'percent' },
      ],
      ranking_complete: false,
    },
    SCM: {
      service_name: 'Banda larga fixa',
      period: '2026-Q2',
      geography: 'BR',
      total_accesses: 55400000,
      fiber_accesses: 44700000,
      provider_market_share: [
        { provider: 'Claro', value: 19.5, unit: 'percent' },
        { provider: 'Vivo', value: 15.1, unit: 'percent' },
        { provider: 'NIO', value: 6.2, unit: 'percent' },
      ],
      ranking_complete: false,
    },
  },
  satisfaction: {
    year: 2025,
    rows: [
      { service: 'internet_fixa', provider: 'Brisanet', isg: 8.28 },
      { service: 'internet_fixa', provider: 'Vivo', isg: 7.78 },
      { service: 'celular_pos_pago', provider: 'Vivo', isg: 7.87 },
      { service: 'celular_pos_pago', provider: 'Claro', isg: 7.72 },
    ],
  },
  sources: [
    {
      source_id: 'ANATEL_COMPETITION_2026Q2',
      service: 'MULTI',
      kind: 'competition_report',
      frequency: 'quarterly',
      landing_url: 'https://www.gov.br/anatel/',
    },
    {
      source_id: 'ANATEL_SATISFACTION_2025',
      service: 'MULTI',
      kind: 'satisfaction',
      frequency: 'annual',
      landing_url: 'https://www.gov.br/anatel/',
    },
  ],
  methodology_notes: [
    'Valores são provenientes de publicações oficiais da Anatel.',
    'Rankings do snapshot são parciais até a ingestão mensal SMP/SCM.',
  ],
}
