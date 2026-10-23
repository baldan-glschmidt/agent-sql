# R088HIT

## Descrição

Cadastro de Histórico de Itinerários de Táxis

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodIti | Number(004,0) | Não | Código do Itinerário |
| DatIni | Date | Não | Data de Início do Histórico de Itinerário |
| HorIni | Number(005,0) | Não | Hora de Início do Histórico de Itinerário |
| ValIti | Number(011,2) | Sim | Valor do Serviço de Táxi no Itinerário |
| DatFim | Date | Sim | Data Final do Histórico de Itinerário |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico de Itinerário |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Histórico de Itinerário |
| DatUsu | Date | Sim | Data da Alteração pelo Usuário |
| HorUsu | Number(005,0) | Sim | Hora da Alteração pelo Usuário |

---

## Chave Primária

- CodPlt
- CodIti
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088HIT_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R088HIT_001

**Tabela:** R088ITI

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodIti | CodIti |

