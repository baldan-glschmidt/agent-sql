# R088VPS

## Descrição

Veículos Prestadores de Serviço

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
| PlaVei | String(010) | Não | Placa do Veículo |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa (Terceiro/Parceiro) |
| NumCon | String(015) | Sim | Número do Contrato de Serviço |

---

## Chave Primária

- PlaVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088VPS_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088VPS_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

