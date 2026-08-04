# E073LVM

## Descrição

Cadastros - Transportadoras - Ligação do Motorista aos veículos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da Transportadora |
| PlaVei | String(010) | Não | Placa do veículo |
| TraMot | Number(009,0) | Não | Código da Transportadora do motorista |
| CodMtr | Number(006,0) | Não | Código do Motorista |
| SitLvm | String(001) | Não | Situação da Ligação |

---

## Chave Primária

- CodTra
- PlaVei
- TraMot
- CodMtr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E073LVM_001

**Tabela:** E073VEI

| Origem | Destino |
|--------|---------|
| CodTra | CodTra |
| PlaVei | PlaVei |

