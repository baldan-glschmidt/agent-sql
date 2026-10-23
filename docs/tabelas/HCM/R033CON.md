# R033CON

## Descrição

Pessoas - Contas Bancárias

---

## Resumo

- Campos: 17
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| DatAlt | Date | Não | Data de Alteração |
| SeqCon | Number(002,0) | Não | Sequência |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| TipBan | Number(001,0) | Sim | Tipo de Conta Bancária |
| ConBan | Number(012,0) | Sim | Conta Bancária |
| DigBan | String(003) | Sim | Dígito da Conta Bancária |
| DatAbe | Date | Sim | Data de Abertura da Conta |
| DatEnc | Date | Sim | Data de Encerramento da Conta |
| EmpAux | Number(004,0) | Sim | USO EXCLUSIVO SENIOR |
| TipAux | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CadAux | Number(009,0) | Sim | USO EXCLUSIVO SENIOR |
| DepAux | Number(002,0) | Sim | USO EXCLUSIVO SENIOR |
| ColAti | Number(001,0) | Sim | USO EXCLUSIVO SENIOR |
| CanAux | Number(007,0) | Sim | USO EXCLUSIVO SENIOR |
| DatAux | Date | Sim | USO EXCLUSIVO SENIOR |

---

## Chave Primária

- CodPes
- DatAlt
- SeqCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033CON_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R033CON_003

**Tabela:** R012BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_R033CON_004

**Tabela:** R012AGE

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |
| CodAge | CodAge |

