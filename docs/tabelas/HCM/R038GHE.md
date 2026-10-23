# R038GHE

## Descrição

Histórico de GHE

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data de início da atuação do colaborador no GHE |
| SeqHis | Number(002,0) | Não | Sequência do Histórico de GHE |
| CodPRA | Number(009,0) | Sim | Código do Cadastro do PGR |
| CodGHE | Number(009,0) | Sim | Código do GHE - Grupo Homogêneo de Exposição |
| DatTer | Date | Sim | Data de término da atuação do Colaborador no GHE |
| ObsHis | String(2000) | Sim | Observação do histórico de GHE |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- SeqHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038GHE_006

**Tabela:** R583GHE

| Origem | Destino |
|--------|---------|
| CodPRA | CodPRA |
| CodGHE | CodGHE |

