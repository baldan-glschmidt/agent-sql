# R016DUL

## Descrição

Dados da Duplicação do Organograma - Locais

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| OrgDes | Number(004,0) | Não | Código do Organograma Destino |
| LocDes | Number(009,0) | Não | Local do Organograma Destino |
| LocOri | Number(009,0) | Não | Local do Organograma Origem |
| LocQua | Number(009,0) | Sim | Local do Quadro de Lotações |
| NovDes | String(060) | Sim | Descrição do Local |

---

## Chave Primária

- OrgDes
- LocDes
- LocOri

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016DUL_000

**Tabela:** R016DUO

| Origem | Destino |
|--------|---------|
| OrgDes | OrgDes |

