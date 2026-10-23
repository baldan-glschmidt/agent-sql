# R110AAF

## Descrição

Acompanhamento de Afastamento

---

## Resumo

- Campos: 22
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodFic | Number(009,0) | Não | Código Ficha Médica |
| DatAco | Date | Não | Data do acompanhamento |
| HorAco | Number(005,0) | Não | Hora do acompanhamento |
| CodAte | Number(006,0) | Sim | Código do atendente responsável pelo acompanhamento |
| DatPer | Date | Sim | Data da perícia |
| RecAlt | String(001) | Sim | Define se recebeu alta da perícia(S/N) |
| CodDoe | String(004) | Sim | Classificação Internacional de Doenças |
| CodCid | String(010) | Sim | Código da Classificação Internacional de Doenças |
| CodSub | String(003) | Sim | Identificação do subgrupo da CID-10 |
| NumBen | String(015) | Sim | Número do benefício |
| AteExt | Number(006,0) | Sim | Código do atendente externo responsável pela perícia |
| NomAte | String(040) | Sim | Nome do atendente externo |
| DatPPe | Date | Sim | Data da próxima perícia |
| ResMed | String(001) | Sim | Indica se o colaborador tem restrição médica(S/N) |
| ObsAte | String(2000) | Sim | Observações do acompanhamento |
| BenRea | String(001) | Sim | Beneficiário reabilitado(S/N) |
| USU_DatAfa | Date | Sim | Data do Afastamento |
| USU_EspEmp | String(006) | Sim | Codigo da Especie do Afastamento Informado pela Empresa |
| USU_EspInss | String(006) | Sim | Codigo da Especie do Afastamento Informado pelo INSS |
| USU_ValIns | Number(011,2) | Sim | Valor Pago INSS |
| USU_DatTer | Date | Sim | Data Termino do Afastamento |

---

## Chave Primária

- NumEmp
- CodFic
- DatAco
- HorAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110AAF_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110AAF_004

**Tabela:** R108TAT

| Origem | Destino |
|--------|---------|
| CodAte | CodAte |

