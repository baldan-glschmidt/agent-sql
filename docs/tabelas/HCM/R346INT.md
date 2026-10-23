# R346INT

## Descrição

eSocial JR - Processo Trabalhista - Informações relativas ao trabalho intermitente

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| PerRef | Date | Não | Mês/ano de referência das informações |
| DiaMes | Number(002,0) | Não | Dia do mês efetivamente trabalhado pelo empregado com contrato de trabalho intermitente |
| HorTra | Number(005,0) | Sim | Horas trabalhadas no dia pelo empregado com contrato de trabalho intermitente |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- PerRef
- DiaMes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R346INT_004

**Tabela:** R346IBC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodPro | CodPro |
| PerRef | PerRef |

