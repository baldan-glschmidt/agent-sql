# R104AUJ

## Descrição

JR - Audiências

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatAud | Date | Não | Data da audiência |
| HorAud | Number(005,0) | Não | Hora da audiência |
| EmpPre | Number(004,0) | Sim | Código da empresa do preposto |
| TipPre | Number(001,0) | Sim | Tipo do colaborador preposto |
| PreAud | Number(009,0) | Sim | Código do colaborador preposto da audiência |
| AndPro | Number(003,0) | Sim | Código do andamento da ação |
| PrvAud | String(250) | Sim | Providências da audiência |
| ObsPrc | String(10000) | Sim | Observações da ação |
| NomArq | String(250) | Sim | Arquivo |
| DatLim | Date | Sim | Data limite definido para tomar as providências referentes à fase do processo. |

---

## Chave Primária

- NumEmp
- CodPrc
- DatAud
- HorAud

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104AUJ_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

