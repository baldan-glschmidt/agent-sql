# R088VEV

## Descrição

Veículos de Visitantes

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |

---

## Chave Primária

- PlaVei
- TipDoc
- NumDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088VEV_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088VEV_002

**Tabela:** R090VIS

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

