# R583INF

## Descrição

Cadastro de Ambientes - Informações

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| DatAlt | Date | Não | Data de alteração das informações do ambiente de trabalho |
| DesAmb | String(8000) | Não | Descrição do ambiente de trabalho |
| CndAmb | String(3000) | Sim | Condições do ambiente de trabalho |

---

## Chave Primária

- NumAmb
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R583INF_000

**Tabela:** R583AMB

| Origem | Destino |
|--------|---------|
| NumAmb | NumAmb |

