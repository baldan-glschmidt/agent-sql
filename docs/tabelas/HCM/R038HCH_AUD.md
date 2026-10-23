# R038HCH_AUD

## Descrição

Auditoria Históricos de Crachás Colaboradores

---

## Resumo

- Campos: 16
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| TipCra | Number(001,0) | Não | Tipo de Crachá |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Titular |
| DatIni | Date | Não | Data de Início do Uso do Crachá |
| HorIni | Number(005,0) | Não | Hora de Início do Uso do Crachá |
| ViaCra | Number(002,0) | Sim | Número da Via do Crachá |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatFim | Date | Sim | Data Final do Uso do Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Uso do Crachá |
| RecEPr | String(030) | Sim | Recibo da Entrega do Provisório |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Crachá |

---

## Chave Primária

- SeqReg
- VerSeq
- TipCra
- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
