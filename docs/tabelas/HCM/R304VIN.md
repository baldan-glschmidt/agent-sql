# R304VIN

## Descrição

e-Sfinge - Dados do Vínculo Inativo

---

## Resumo

- Campos: 20
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumMat | String(016) | Não | Número da matrícula do agente público na Unidade |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na Receita Federal |
| DatVig | Date | Não | Data de início da vigência da nova situação de vínculo que está sendo registrada |
| SeqReg | Number(009,0) | Não | Sequência |
| NomCar | String(100) | Não | Nome do cargo da unidade de origem do agente público |
| EspVin | Number(002,0) | Não | Espeficicação do Vínculo do Agente Público Inativo com a Unidade |
| PidSta | String(030) | Sim | Pid Status |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(008,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(008,0) | Sim | Campo Auxiliar 5 |
| CmpAu6 | Number(008,0) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(002) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(002) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(2000) | Sim | Campo Auxiliar 9 |
| CodUgo | Number(005,0) | Sim | Código da unidade gestora de origem do inativo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- NumMat
- NumCpf
- DatVig
- SeqReg

---

## Índices

### R304VINIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

### IR_R304VIN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

