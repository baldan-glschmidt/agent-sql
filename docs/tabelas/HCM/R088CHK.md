# R088CHK

## Descrição

Manutenções Programadas

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| MarVei | String(015) | Não | Marca do Veículo |
| ModVei | String(015) | Não | Modelo do Veículo |
| CodPec | Number(006,0) | Não | Código da Peça/Serviço em Manutenção |
| PerIod | Number(007,0) | Sim | Período de Manutenção. |
| PerQlm | Number(007,0) | Sim | Quilometragem Verificação |
| ObsChk | String(080) | Sim | Observação da Manutenção |

---

## Chave Primária

- MarVei
- ModVei
- CodPec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088CHK_002

**Tabela:** R088PEC

| Origem | Destino |
|--------|---------|
| CodPec | CodPec |

