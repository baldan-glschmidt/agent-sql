# R009PEN

## Descrição

Gestão de Incidentes - Penalidades

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(003,0) | Não | Código da Penalidade |
| DesPen | String(040) | Sim | Descrição da Penalidade |
| RelPen | Number(003,0) | Sim | Relevância da Penalidade |
| GerAfa | String(001) | Sim | Penalidade Gera Afastamento |
| SitAfa | Number(003,0) | Sim | Situação de Afastamento para Penalidade |
| DiaAfa | Number(002,0) | Sim | Duração do Afastamento em Dias |
| ExiNot | String(001) | Sim | Exige Descrição Anotação da Ficha Registro |
| TipNot | Number(003,0) | Sim | Tipo de Anotação da Ficha Registro |
| GerDoc | String(001) | Sim | Gera Documento de Penalidade |
| ModDoc | String(020) | Sim | Modelo de Documento da Penalidade |

---

## Chave Primária

- CodPen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R009PEN_004

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitAfa | CodSit |

