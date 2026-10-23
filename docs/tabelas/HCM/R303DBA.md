# R303DBA

## Descrição

e-Sfinge - Dados Bancários para Crédito dos Proventos

---

## Resumo

- Campos: 16
- Chave Primária: 9 campo(s)
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
| SeqFop | Number(002,0) | Não | Número Sequêncial da Folha de Pagamento |
| FolEsf | Number(002,0) | Não | Tipo de folha de pagamento e-Sfinge |
| IndCon | String(001) | Sim | Indicativo Conta Bancária |
| CodBan | Number(004,0) | Sim | Código do Banco |
| AgeBan | Number(006,0) | Sim | Código da Agência Bancária |
| ConBan | String(015) | Sim | Código da Conta Bancária |
| UniOrc | Number(005,0) | Não | Código da Unidade Orçamentária pagadora do provento |
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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R303DBA_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

