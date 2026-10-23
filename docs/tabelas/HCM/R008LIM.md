# R008LIM

## Descrição

Limites do Evento

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| SeqReg | Number(002,0) | Não | Sequência do Limite |
| ConSit | Number(001,0) | Sim | Considerar Soma das Situações no Limite |
| DimMin | String(001) | Sim | Diminuir Limite Mínimo |
| LimMin | Number(010,0) | Sim | Limite Mínimo de Horas |
| LimMax | Number(010,0) | Sim | Limite Máximo de Horas |
| NumEmp | Number(004,0) | Sim | Código Empresa |
| AbrFil | String(100) | Sim | Abrangência de Filial |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| AbrCar | String(100) | Sim | Abrangência de Cargo |
| AbrEsc | String(100) | Sim | Abrangência de Escala |

---

## Chave Primária

- CodTab
- CodEve
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008LIM_001

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

