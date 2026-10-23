# R303VIP

## Descrição

e-Sfinge - Dados do Vínculo de Pensionista

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
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
| NumMat | String(016) | Não | Número da matrícula do Pensionista na Unidade |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na Receita Federal |
| DatVig | Date | Não | Data de início da vigência da nova situação de vínculo que está sendo registrada |
| VinPen | Number(002,0) | Não | Espeficicação do Vínculo de Pensionista com a Unidade |
| CpfIns | Number(011,0) | Não | Código de identif. do contribuinte na Receita Federal do instituidor de pensão |
| NomIns | String(100) | Não | Nome completo do instituidor de pensão |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipCol
- NumCad
- NumMat
- NumCpf
- DatVig

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R303VIP_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

