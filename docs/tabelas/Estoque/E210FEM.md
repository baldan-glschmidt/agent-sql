# E210FEM

## Descrição

Estoques - Faixa de Evolução do Estoque Mínimo Automatizado

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| SeqFem | Number(002,0) | Não | Sequência da faixa de evolução do estoque mínimo automatizado |
| QtmIni | Number(014,5) | Sim | Quantidade estoque mínimo atual inicial |
| QtmFin | Number(014,5) | Sim | Quantidade estoque mínimo atual final |
| PerAum | Number(005,2) | Sim | Percentual de aumento do estoque mínimo automatizado |
| PerRed | Number(005,2) | Sim | Percentual de redução do estoque mínimo automatizado |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- SeqFem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E210FEM_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

