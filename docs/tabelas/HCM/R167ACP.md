# R167ACP

## Descrição

BS - Pacote de Benefícios - Auxílio Creche

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
| CodPac | Number(004,0) | Não | Código do Pacote de Benefícios |
| IdaMin | Number(002,0) | Não | Idade Mínima Dependente |
| IdaMax | Number(002,0) | Não | Idade Máxima Dependente |
| ValRee | Number(011,2) | Sim | Valor de Reembolso |

---

## Chave Primária

- CodPac
- IdaMin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R167ACP_000

**Tabela:** R167CPB

| Origem | Destino |
|--------|---------|
| CodPac | CodPac |

