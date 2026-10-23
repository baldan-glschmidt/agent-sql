# R015ASD

## Descrição

Prêmio Assiduidade

---

## Resumo

- Campos: 3
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| SitAsd | Number(003,0) | Sim | Situação do Prêmio Assiduidade |
| TpoGoz | Number(003,0) | Sim | Meses para Gozar o Prêmio Assiduidade |

---

## Chave Primária

- CodSin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R015ASD_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

### IR_R015ASD_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| SitAsd | CodSit |

