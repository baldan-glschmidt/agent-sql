# R146DEF

## Descrição

Provisão - Definições Gerais da Provisão

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| DesPrv | String(100) | Sim | Descrição da Provisão |
| TotAvo | Number(002,0) | Sim | Total de Avos |
| BaiFor | String(001) | Sim | Tipo da Baixa da Provisão |
| LimAvo | Number(002,0) | Sim | Limite de Avos Para Zerar o Saldo do Período |
| CodTab | Number(003,0) | Sim | Código Tabela de Eventos |
| TipSis | String(001) | Sim | Tipo de Sistema |
| VerAfa | String(001) | Sim | Considera Afastamentos |
| BaiSld | String(001) | Sim | Baixar Saldo da Provisão na Rescisão |
| CalPrv | String(001) | Sim | Calcular Provisão Mensal |
| UsaSld | String(001) | Sim | Controlar Saldo Transferido Entre Empresas |
| RegCal | Number(003,0) | Sim | Código da Regra de Cálculo |

---

## Chave Primária

- TipPrv

---

## Índices

### R146DEFIndice2

**Tipo:** Unico

Campos:
- TipPrv
- CodTab

---

## Relacionamentos

Nenhum relacionamento cadastrado.
