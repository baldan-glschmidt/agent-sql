# R070PEV_AUD

## Descrição

Auditoria Permissão Alternativa Visitante

---

## Resumo

- Campos: 15
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| TipDoc | Number(001,0) | Não | Tipo de Documento |
| NumDoc | String(020) | Não | Número do Documento |
| DatIni | Date | Não | Data Inicial da Permissão Alternativa |
| HorIni | Number(005,0) | Não | Hora Inicial da Permissão Alternativa |
| CodPrm | Number(005,0) | Não | Código da Permissão Alternativa |
| DatFim | Date | Sim | Data Final da Permissão Alternativa |
| HorFim | Number(005,0) | Sim | Hora Final da Permissão Alternativa |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Permissão |
| NumEmp | Number(004,0) | Sim | Empresa do Responsável |
| TipCol | Number(001,0) | Sim | Tipo Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Responsável |
| ObsPrm | String(080) | Sim | Observação |
| StaAcc | Number(001,0) | Sim | Status da Área Restrita |

---

## Chave Primária

- SeqReg
- VerSeq
- TipDoc
- NumDoc
- DatIni
- HorIni
- CodPrm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
