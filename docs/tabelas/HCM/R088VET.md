# R088VET

## Descrição

Veículos de Teste

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| MarVei | String(015) | Não | Marca do Veículo |
| ModVei | String(015) | Não | Modelo do Veículo |
| NumCha | String(020) | Não | Número do Chassi |
| CorVei | String(015) | Sim | Cor do Veículo |
| AnoVei | Number(004,0) | Sim | Ano de Fabricação do Veículo |
| TipVei | Number(002,0) | Sim | Tipo de Veículo |
| ObsVei | String(080) | Sim | Observação do Veículo |

---

## Chave Primária

- MarVei
- ModVei
- NumCha

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088VET_000

**Tabela:** R088MAR

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |

### IR_R088VET_001

**Tabela:** R088MOD

| Origem | Destino |
|--------|---------|
| MarVei | MarVei |
| ModVei | ModVei |

