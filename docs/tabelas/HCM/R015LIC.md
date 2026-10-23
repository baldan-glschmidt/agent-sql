# R015LIC

## Descrição

Licença Especial

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| MesPfe | Number(003,0) | Sim | Meses do Período Aquisitivo da Licença Especial |
| MinPrr | Number(004,0) | Sim | Mínimo de Dias de Prorrogação no Período |
| MaxPrr | Number(004,0) | Sim | Máximo de Dias de Prorrogação no Período |
| MaxPda | Number(003,0) | Sim | Máximo de Dias Até Perder o Período Aquisitivo |
| TpoGoz | Number(003,0) | Sim | Meses para Gozar a Licença Especial |
| TipLic | Number(001,0) | Sim | Tipo de Licença |
| SitLic | Number(003,0) | Sim | Situação da Licença Especial |
| TrtRcs | Number(001,0) | Sim | Tratamento da Licença Especial na Rescisão |
| PrvLic | String(001) | Sim | Provisionar Licença |

---

## Chave Primária

- CodSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R015LIC_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

### IR_R015LIC_007

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitLic | CodSit |

