# R110NIV

## Descrição

Nível de Atenção - Subnormalidade

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
| CodCon | Number(002,0) | Não | Código da tabela de controle do nível de atenção |
| NivAte | Number(002,0) | Não | Código do nível de atenção |
| DesNiv | String(020) | Sim | Descrição do nível de atenção |
| CorSun | String(010) | Sim | Cor da subnormalidade |

---

## Chave Primária

- CodCon
- NivAte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110NIV_000

**Tabela:** R110CON

| Origem | Destino |
|--------|---------|
| CodCon | CodCon |

