# E073LVV

## Descrição

Cadastros - Transportadoras - Ligação do Cavalo ao Reboque

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da Transportadora |
| PlaCav | String(010) | Não | Placa do cavalo |
| TraReb | Number(009,0) | Não | Código da transportadora do reboque |
| PlaReb | String(010) | Não | Placa do reboque |
| SitLvv | String(001) | Não | Situação da ligação |

---

## Chave Primária

- CodTra
- PlaCav
- TraReb
- PlaReb

---

## Índices

### E073LVVIndice1

**Tipo:** Não unico

Campos:
- TraReb
- PlaReb

---

## Relacionamentos

### IR_E073LVV_001

**Tabela:** E073VEI

| Origem | Destino |
|--------|---------|
| CodTra | CodTra |
| PlaCav | PlaVei |

### IR_E073LVV_003

**Tabela:** E073VEI

| Origem | Destino |
|--------|---------|
| TraReb | CodTra |
| PlaReb | PlaVei |

