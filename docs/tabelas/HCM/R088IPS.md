# R088IPS

## Descrição

Parcelas de Impostos IPVA e Seguro Obrigatório

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatVen | Date | Não | Data Vencimento |
| TipSeg | Number(001,0) | Não | Tipo de Seguro |
| EmpIps | Number(008,0) | Sim | Código da Outra Empresa |
| ValSeg | Number(011,2) | Sim | Valor Segurado |
| SitSeg | Number(001,0) | Sim | Situação Seguro |
| HorVen | Number(005,0) | Sim | Hora Vencimento |
| SeqVen | Number(002,0) | Sim | Sequência de Cadastro de Impostos de Veículos |

---

## Chave Primária

- PlaVei
- DatVen
- TipSeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088IPS_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

