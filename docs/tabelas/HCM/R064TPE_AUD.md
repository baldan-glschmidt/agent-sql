# R064TPE_AUD

## Descrição

Auditoria Troca de Permissão

---

## Resumo

- Campos: 18
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(015,0) | Não | Sequencia do Registro |
| VerSeq | Number(010,0) | Não | Versão da Sequencia |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial da Troca de Permissão |
| HorIni | Number(005,0) | Não | Hora Inicial da Troca de Permissão |
| DatFim | Date | Sim | Data Final da Troca de Permissão |
| HorFim | Number(005,0) | Sim | Hora Final da Troca de Permissão |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso para os Dias Normais |
| PrmFer | Number(005,0) | Sim | Permissão de Acesso para os Feriados |
| PrmSab | Number(005,0) | Sim | Permissão de Acesso para os Sábados |
| PrmDom | Number(005,0) | Sim | Permissão de Acesso para os Domingos |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Troca de Permissão |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador da Troca de Permissão |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Troca de Permissão |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Programação |

---

## Chave Primária

- SeqReg
- VerSeq
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
