# R070PEC_AUD

## Descrição

Auditoria Permissão Alternativa Colaborador

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro Colaborador |
| DatIni | Date | Sim | Data Inicial da Permissão Alternativa |
| HorIni | Number(005,0) | Sim | Hora Inicial da Permissão Alternativa |
| CodPrm | Number(005,0) | Sim | Código da Permissão Alternativa |
| DatFim | Date | Sim | Data Final da Permissão Alternativa |
| HorFim | Number(005,0) | Sim | Hora Final da Permissão Alternativa |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Permissão |
| ObsPrm | String(080) | Sim | Observação |
| StaAcc | Number(001,0) | Sim | Status da Área Restrita |

---

## Chave Primária

- SeqReg
- VerSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
