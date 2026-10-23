# R058FAG

## Descrição

Faixas de Acesso de Grupo de Coletores

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPrm | Number(005,0) | Não | Código da Permissão |
| CodGrr | Number(003,0) | Não | Código do Grupo de Coletores |
| IniFai | Number(005,0) | Não | Início da Faixa p/ Marcação de Acesso |
| FimFai | Number(005,0) | Sim | Fim da Faixa p/ Marcação de Acesso |

---

## Chave Primária

- CodPrm
- CodGrr
- IniFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058FAG_000

**Tabela:** R058PRM

| Origem | Destino |
|--------|---------|
| CodPrm | CodPrm |

### IR_R058FAG_001

**Tabela:** R058GRR

| Origem | Destino |
|--------|---------|
| CodGrr | CodGrr |

