# R064TPE

## Descrição

Troca de Permissão

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
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
| SeqReg | Number(015,0) | Sim | Sequencia do Registro |

---

## Chave Primária

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

### IR_R064TPE_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

