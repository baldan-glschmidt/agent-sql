# R073HCR

## Descrição

Histórico de Crachás Responsáveis do Aluno

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipCra | Number(001,0) | Não | Tipo de Crachá |
| TipDoc | Number(001,0) | Não | Tipo do Documento do Responsável |
| NumDoc | String(020) | Não | Número do Documento do Responsável |
| DatIni | Date | Não | Data Inicial do Histórico do Crachá |
| HorIni | Number(005,0) | Não | Hora Inicial do Histórico de Crachá |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatFim | Date | Sim | Data Final do Histórico de Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico de Crachá |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Crachá |

---

## Chave Primária

- TipCra
- TipDoc
- NumDoc
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073HCR_002

**Tabela:** R073RES

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

