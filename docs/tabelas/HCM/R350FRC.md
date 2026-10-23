# R350FRC

## Descrição

S-2240 - eSocial - Condições Ambientais do Trabalho - Agentes Nocivos

---

## Resumo

- Campos: 29
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data em que o trabalhador iniciou as atividades no ambiente de trabalho |
| SeqCon | Number(009,0) | Não | Sequência |
| SeqFrc | Number(009,0) | Não | Sequência Fator Risco |
| CodFat | String(009) | Sim | Código do agente nocivo ao qual o trabalhador está exposto |
| DesRis | String(999) | Sim | Descrição do agente nocivo |
| TipAva | Number(001,0) | Sim | Tipo de avaliação do fator de risco |
| IntCon | Number(010,4) | Sim | Intensidade, concentração ou dose da exposição do trabalhador |
| LimTol | Number(010,4) | Sim | Limite de tolerância calculado para agentes específicos |
| UniMed | Number(002,0) | Sim | Dose ou unidade de medida da intensidade ou concentração do agente |
| TecMed | String(040) | Sim | Técnica utilizada para medição da intensidade ou concentração |
| ConIns | String(001) | Sim | Insalubridade (Obsoleto) |
| ConPer | String(001) | Sim | Periculosidade (Obsoleto) |
| ApoEsp | String(001) | Sim | Aposentadoria Especial (Obsoleto) |
| UtiEpc | Number(001,0) | Sim | A empresa implementa medidas de proteção coletiva (EPC) para eliminar ou reduzir a exposição dos trabalhadores ao fator de risco? |
| EfiEpc | String(001) | Sim | Os EPCs são eficazes na neutralização dos riscos ao trabalhador? |
| UtiEpi | Number(001,0) | Sim | Utilização de EPI |
| EfiEpi | String(001) | Sim | Os EPIs são eficazes na neutralização do risco ao trabalhador? |
| MedPro | String(001) | Sim | Foi tentada a implementação de medidas de proteção coletiva? |
| ConFun | String(001) | Sim | Foram observadas as condições de funcionamento do EPI ao longo do tempo? |
| UsoIni | String(001) | Sim | Foi observado o uso ininterrupto do EPI ao longo do tempo? |
| PraVal | String(001) | Sim | Foi observado o prazo de validade do Certificado de Aprovação - CA do MTb? |
| PerTro | String(001) | Sim | É observada a periodicidade de troca definida pelo fabricante nacional ou importador e/ou programas ambientais? |
| ObsHig | String(001) | Sim | É observada a higienização conforme orientação do fabricante nacional ou importador? |
| NumPro | String(021) | Sim | Número do processo, em caso de agente nocivo incluído por determinação judicial |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatIni
- SeqCon
- SeqFrc

---

## Índices

### R350FRCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
