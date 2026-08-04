# E099PAS

## Descrição

Cadastros - Usuários - Parâmetros Fluxo de Caixa (2) - Distribuição Títulos Anteriores

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| SeqPas | Number(003,0) | Não | Sequência de registro |
| RecIni | Number(003,0) | Sim | Sequência inicial do dia a considerar o percentual para o CR |
| RecFim | Number(003,0) | Sim | Sequência final do dia a considerar o percentual para o CR |
| RecPdi | Number(005,2) | Sim | Percentual a distribuir dos títulos a receber com vencimentos anteriores |
| PagIni | Number(003,0) | Sim | Sequência inicial do dia a considerar o percentual para o CP |
| PagFim | Number(003,0) | Sim | Sequência final do dia a considerar o percentual para o CP |
| PagPdi | Number(005,2) | Sim | Percentual a distribuir dos títulos a pagar com vencimentos anteriores |

---

## Chave Primária

- CodEmp
- CodUsu
- SeqPas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099PAS_001

**Tabela:** E099PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

