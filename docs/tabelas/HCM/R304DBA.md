# R304DBA

## Descrição

e-Sfinge - Dados Bancários para Crédito dos Proventos

---

## Resumo

- Campos: 25
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na Receita Federal |
| NumMat | String(016) | Não | Número da matrícula na Unidade |
| AnoMes | Date | Não | Mês e Ano da Folha de Pagamento |
| SeqFop | Number(002,0) | Não | Número Sequêncial da Folha de Pagamento |
| SeqReg | Number(009,0) | Não | Sequência Dados Bancários |
| FolEsf | Number(002,0) | Não | Tipo de folha de pagamento e-Sfinge |
| ComSup | Date | Sim | Ano/Mês da competência da folha de pagamento suplementar |
| IndCon | String(001) | Sim | Indicativo Conta Bancária |
| CodBan | Number(004,0) | Sim | Código do Banco |
| AgeBan | Number(006,0) | Sim | Código da Agência Bancária |
| ConBan | String(015) | Sim | Código da Conta Bancária |
| UniOrc | Number(005,0) | Não | Código da Unidade Orçamentária pagadora do provento |
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

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- NumCpf
- NumMat
- AnoMes
- SeqFop
- SeqReg

---

## Índices

### R304DBAIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

### IR_R304DBA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

