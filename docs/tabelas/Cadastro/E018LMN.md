# E018LMN

## Descrição

Motivos de Parada - Ligação com Equipamento e Serviço de Manutenção

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMtv | String(004) | Não | Código do motivo de parada |
| CodEqp | String(020) | Não | Código do equipamento/ferramenta afetado pelo serviço de manutenção |
| CodSer | String(014) | Não | Código do serviço de manutenção |
| GerPar | String(001) | Não | Indicativo se gera parada a partir de manutenção com o serviço e no equipamento |

---

## Chave Primária

- CodEmp
- CodMtv
- CodEqp
- CodSer

---

## Índices

### E018LMNIndiceEqpSer

**Tipo:** Não unico

Campos:
- CodEmp
- CodEqp
- CodSer
- GerPar

---

## Relacionamentos

### IR_E018LMN_001

**Tabela:** E018MTV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMtv | CodMtv |

