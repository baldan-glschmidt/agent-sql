# R088SEG

## Descrição

Seguros de Veículos

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| CodCrr | Number(004,0) | Sim | Código do Corretor |
| NumApo | String(020) | Sim | Número da Apólice Seguro |
| TipCob | Number(002,0) | Sim | Tipo Cobertura |
| DatIni | Date | Sim | Data de Início da Vígência  do Seguro |
| DatVal | Date | Sim | Data de Validade do Seguro |
| ValSeg | Number(011,2) | Sim | Valor Segurado |
| DesFra | String(080) | Sim | Descrição Franquia |
| ObsSeg | String(080) | Sim | Observação do Seguro do Veículo |

---

## Chave Primária

- PlaVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088SEG_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

