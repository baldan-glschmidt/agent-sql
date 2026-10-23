# R303VIN

## Descrição

e-Sfinge - Dados do Vínculo Inativo

---

## Resumo

- Campos: 11
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
| NumMat | String(016) | Não | Número da matrícula do agente público na Unidade |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na Receita Federal |
| DatVig | Date | Não | Data de início da vigência da nova situação de vínculo que está sendo registrada |
| NomCar | String(100) | Não | Nome do cargo da unidade de origem do agente público |
| EspVin | Number(002,0) | Não | Espeficicação do Vínculo do Agente Público Inativo com a Unidade |
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

### IR_R303VIN_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

