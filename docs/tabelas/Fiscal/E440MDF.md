# E440MDF

## Descrição

Compras - Notas Fiscais de Entrada - Manifesto Documento Fiscal

---

## Resumo

- Campos: 57
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSma | String(003) | Não | Código da série do manifesto |
| NumMan | Number(009,0) | Não | Número do manifesto |
| CodTra | Number(009,0) | Sim | Código da Transportadora |
| PlaVei | String(010) | Sim | Placa do veículo |
| CodMtr | Number(006,0) | Sim | Código do motorista |
| Vlrliq | Number(015,2) | Sim | Total líquido do manifesto |
| UniMed | String(003) | Sim | Unidade de medida |
| PesBru | Number(014,5) | Sim | Peso bruto do manifesto |
| ObsMan | String(4999) | Sim | Observação do manifesto |
| SitMan | Number(001,0) | Sim | Situação do manifesto |
| DatEmm | Date | Sim | Data de emissão do manifesto |
| HorEmm | Number(005,0) | Sim | Hora de emissão do manifesto |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| CodAgp | String(020) | Sim | Código de agendamento no porto |
| DatSai | Date | Sim | Data da saída do embarque |
| HorSai | Number(005,0) | Sim | Hora da saída do embarque |
| NumCio | String(030) | Sim | Informação do código identificador da operação de transporte (CIOT) |
| IndPos | String(001) | Sim | Indicativo de carregamento posterior |
| TipVia | String(001) | Sim | Indicativo de Modalidade de Transporte |
| MarNac | String(004) | Sim | Marca da Nacionalidade da Aeronave (Modalidade Aéreo) |
| MarMat | String(006) | Sim | Marca de Matrícula da Aeronave (Modalidade Aéreo) |
| NumVoo | String(009) | Sim | Número do Vôo (Modalidade Aéreo) |
| AerEmb | String(004) | Sim | Aeródromo de Embarque (Modalidade Aéreo) |
| AerDes | String(004) | Sim | Aeródromo de Destino (Modalidade Aéreo) |
| DatVoo | Date | Sim | Data do Vôo (Modalidade Aéreo) |
| TipEmt | Number(002,0) | Sim | Tipo do Emitente |
| TipCga | Number(002,0) | Sim | Tipo de Carga |
| CodPro | String(014) | Sim | Produto Predominante |
| CodDer | String(007) | Sim | Código da Derivação do Produto Predominante |
| PprDes | String(050) | Sim | Descrição Produto Predominante |
| PprGti | String(020) | Sim | GTIN Produto Predominante |
| PprNcm | String(010) | Sim | NCM Produto Predominante |
| CatCve | Number(002,0) | Sim | Categoria de Combinação Veicular |
| TraReb | Number(009,0) | Sim | Código da transportadora do reboque |
| PlaReb | String(010) | Sim | Placa do reboque |
| TraRe2 | Number(009,0) | Sim | Código da transportadora do reboque 2 |
| PlaRe2 | String(010) | Sim | Placa do reboque 2 |
| TraRe3 | Number(009,0) | Sim | Código da transportadora do reboque 3 |
| PlaRe3 | String(010) | Sim | Placa do reboque 3 |
| NomPag | String(060) | Sim | Razão social ou Nome do responsável pelo pagamento |
| TipRpg | String(001) | Sim | Indicativo do tipo de pessoa do responsável pelo pagamento (Jurídica ou Física) |
| CgcPag | String(014) | Sim | Número do CNPJ ou CPF do responsável pelo pagamento |
| NumIdf | String(040) | Sim | Número de identificação fiscal |
| VlrCtr | Number(015,2) | Sim | Valor Total do Contrato |
| AltDes | String(001) | Sim | Indicador de operação de transporte de alto desempenho |
| IndPag | String(001) | Sim | Indicativo da forma de pagamento |
| VlrAdi | Number(015,2) | Sim | Valor do Adiantamento para pagamento a prazo |
| IndAnt | String(001) | Sim | Indicador para declarar concordância em antecipar o adiantamento |
| TipAtp | Number(001,0) | Sim | Tipo de Permissão em relação a antecipação das parcelas |
| CodBan | String(005) | Sim | Número do banco |
| CodAge | String(010) | Sim | Número da agência bancária |
| CgcIpe | String(014) | Sim | Número do CNPJ da Instituição de Pagamento Eletrônico do Frete |
| ChvPix | String(060) | Sim | Chave PIX |

---

## Chave Primária

- CodEmp
- CodFil
- CodSma
- NumMan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
