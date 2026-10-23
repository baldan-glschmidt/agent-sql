# R102THF

## Descrição

Turnos/Horários Filiais SESMT

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do SESMT |
| CodSmt | Number(004,0) | Não | Código do SESMT |
| DatAlt | Date | Não | Data de Alteração |
| CodFil | Number(006,0) | Não | Filial do SESMT |
| SeqThf | Number(002,0) | Não | Sequência |
| DesThf | String(200) | Sim | Descrição do Turno/Horário de Trabalho da Filial |

---

## Chave Primária

- NumEmp
- CodSmt
- DatAlt
- CodFil
- SeqThf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102THF_001

**Tabela:** R102SMT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodSmt | CodSmt |

### IR_R102THF_003

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

