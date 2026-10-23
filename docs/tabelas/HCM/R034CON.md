# R034CON

## Descrição

Contas Bancárias

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatAlt | Date | Não | Data de Alteração |
| SeqCon | Number(002,0) | Não | Sequência |
| CodBan | Number(004,0) | Não | Código do Banco |
| CodAge | Number(005,0) | Não | Código da Agência |
| TipBan | Number(001,0) | Sim | Tipo de Conta Bancária |
| ConBan | Number(012,0) | Não | Conta Bancária |
| DigBan | String(003) | Sim | Dígito da Conta Bancária |
| PerCon | Number(005,2) | Sim | Percentual da Conta Bancária |
| CodOpe | Number(004,0) | Sim | Código de Operação da Conta Bancária |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt
- SeqCon
- CodBan
- CodAge
- ConBan

---

## Índices

### R034CONIndice2

**Tipo:** Não unico

Campos:
- CodBan
- CodAge

---

## Relacionamentos

### IR_R034CON_005

**Tabela:** R012BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_R034CON_006

**Tabela:** R012AGE

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |
| CodAge | CodAge |

