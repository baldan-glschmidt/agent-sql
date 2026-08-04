# E019RED

## Descrição

Tabelas - Redução de Impostos - Por Estado

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTrd | String(003) | Não | Código de redução de impostos |
| TipImp | Number(002,0) | Não | Tipo de imposto a ser reduzido |
| SigUfs | String(002) | Não | Sigla do estado |
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| RedSai | Number(008,5) | Sim | Percentual de redução/acréscimo da base do imposto nas saídas para contribuinte |
| RedSnc | Number(008,5) | Sim | Percentual de redução/acréscimo da base do imposto nas saídas para não contribuinte |
| RedEnt | Number(008,5) | Sim | Percentual de redução/acréscimo na base do imposto nas entradas de contribuinte |
| RedEnc | Number(008,5) | Sim | Percentual de redução/acréscimo na base do imposto nas entradas de não contribuinte |
| CodMsg | Number(004,0) | Sim | Código da mensagem associada a redução do imposto |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodMs2 | Number(004,0) | Sim | Código da mensagem - 2 associada ao ICMS especial |
| CodMs3 | Number(004,0) | Sim | Código da mensagem - 3 associada ao ICMS especial |
| CodMs4 | Number(004,0) | Sim | Código da mensagem - 4 associada ao ICMS especial |
| MotRmo | Number(002,0) | Sim | Motivo de redução de Alíquota de ICMS Monofásico |

---

## Chave Primária

- CodTrd
- TipImp
- SigUfs
- CodEmp
- CodFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E019RED_000

**Tabela:** E019TRD

| Origem | Destino |
|--------|---------|
| CodTrd | CodTrd |

