# R303FOP

## Descrição

e-Sfinge - Folha de Pagamento

---

## Resumo

- Campos: 15
- Chave Primária: 11 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na Receita Federal |
| NumMat | String(016) | Não | Número da matrícula na Unidade |
| AnoMes | Date | Não | Mês e Ano da Folha de Pagamento |
| SeqFop | Number(002,0) | Não | Número Sequencial da Folha de Pagamento |
| CodCom | String(016) | Não | Código do Componente da Folha de Pagamento Conforme Tabela Componentes da Folha Pagamento |
| IndVer | String(001) | Não | Indicativo de verba paga ou descontada do servidor - Provento ou Desconto (P,D) |
| FolEsf | Number(002,0) | Não | Tipo de folha de pagamento e-Sfinge |
| ValCom | Number(014,2) | Não | Valor lançado (pago ou descontado) para o componente na folha de pagamento |
| CodCal | Number(005,0) | Sim | Código de Cálculo correspondente no sistema |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipCol
- NumCad
- NumCpf
- NumMat
- AnoMes
- SeqFop
- CodCom
- IndVer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R303FOP_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

