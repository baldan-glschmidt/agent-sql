# E073LVR

## Descrição

Cadastros - Transportadoras - Ligação do Veículo às Rotas de Entrega

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da Transportadora |
| PlaVei | String(010) | Não | Placa do veículo |
| CodRoe | String(003) | Não | Código da Rota ou Localidade do Cliente |
| SitLvr | String(001) | Sim | Situação da ligação veículo x rotas de entrega |

---

## Chave Primária

- CodTra
- PlaVei
- CodRoe

---

## Índices

### E073LVRIndice1

**Tipo:** Não unico

Campos:
- CodRoe

---

## Relacionamentos

### IR_E073LVR_000

**Tabela:** E073TRA

| Origem | Destino |
|--------|---------|
| CodTra | CodTra |

### IR_E073LVR_001

**Tabela:** E073VEI

| Origem | Destino |
|--------|---------|
| CodTra | CodTra |
| PlaVei | PlaVei |

### IR_E073LVR_002

**Tabela:** E062ROE

| Origem | Destino |
|--------|---------|
| CodRoe | CodRoe |

