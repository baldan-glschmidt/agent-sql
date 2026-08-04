# E055NRE

## Descrição

Tabelas - Reinf - Natureza de Rendimentos

---

## Resumo

- Campos: 34
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| NatRen | String(009) | Não | Natureza Rendimentos |
| DesRen | String(250) | Sim | Descrição Natureza Rendimentos |
| IndFci | String(001) | Sim | Fundo ou Clube de Investimento |
| IndDet | String(001) | Sim | 13º Salario |
| IndRra | String(001) | Sim | Rendimentos Recebidos Acumuladamente |
| CodDed | String(100) | Sim | Deduções |
| CodIse | String(100) | Sim | Rendimentos Isentos |
| IndPfb | String(001) | Sim | Beneficiário Pessoa Física residente fiscal no Brasil |
| IndPjb | String(001) | Sim | Beneficiário Pessoa Jurídica residente fiscal no Brasil |
| IndPfe | String(001) | Sim | Beneficiário Pessoa Física residente fiscal no Exterior |
| IndPje | String(001) | Sim | Beneficiário Pessoa Jurídica residente fiscal no Exterior |
| SitTri | String(100) | Sim | Tributo |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| FatIPF | String(001) | Sim | Fato gerador imposto renda pessoa física |
| FatIPJ | String(001) | Sim | Fato gerador imposto renda pessoa jurídica |
| RetCon | String(001) | Sim | Retenção das contribuições sociais |
| AgrImp | String(001) | Sim | Agrupar Impostos no Valor Agregado |
| RetIRB | String(009) | Sim | Código da Retenção IR |
| RetIRE | String(009) | Sim | Código da Retenção IR Exterior |
| RetIRC | String(009) | Sim | Código da Retenção IR Classificação Tributária 85 |
| RetCSL | String(009) | Sim | Código da Retenção CSLL |
| RetCSC | String(009) | Sim | Código da Retenção CSLL Classificação Tributária 85 |
| RetCOF | String(009) | Sim | Código da Retenção COFINS |
| RetCOC | String(009) | Sim | Código da Retenção COFINS Classificação Tributária 85 |
| RetPPN | String(009) | Sim | Código da Retenção PP |
| RetPPC | String(009) | Sim | Código da Retenção PP Classificação Tributária 85 |
| RetAGR | String(009) | Sim | Código da Retenção Agregado |
| RetAGC | String(009) | Sim | Código da Retenção Agregado Classificação Tributária 85 |

---

## Chave Primária

- IdeUni

---

## Índices

### E055NREIndice2

**Tipo:** Unico

Campos:
- NatRen

---

## Relacionamentos

Nenhum relacionamento cadastrado.
