# E008GDM

## Descrição

Tabelas - Cidades para RAIS - Parâmetros para geração das DESIF

---

## Resumo

- Campos: 31
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRai | Number(007,0) | Não | Código da cidade RAIS utilizada para apuração do ISS |
| DatIni | Date | Não | Data de início de vigência |
| TipDec | Number(002,0) | Sim | Tipo de Declaração |
| VerDec | String(030) | Sim | Versão da Declaração |
| ObsDec | String(250) | Sim | Observação da Declaração |
| CodImp | String(003) | Sim | Código do imposto |
| TipCtb | String(001) | Sim | Tipo Conta Contábil a ser Exportada |
| CodMpc | Number(004,0) | Sim | Modelo Plano Cosif |
| TipPlc | Number(002,0) | Sim | Tipo de Exportação das Partidas dos Lançamentos Contábeis |
| ExpLct | String(001) | Sim | Exportar Módulo 1 apenas para a filial que possui contabilidade própria |
| LisCrd | Number(001,0) | Sim | Tipos conta do plano COSIF que serão exportadas |
| CodAce | String(070) | Sim | Código de acesso ao site da prefeitura |
| CgcPrf | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da prefeitura |
| DocIdePrf | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da prefeitura |
| CodDec | Number(009,0) | Sim | Código da declaração |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| GuiUni | String(001) | Sim | Indicativo se guia de recolhimento da apuração do ISS próprio será unificada |
| RegRet | String(001) | Sim | Indica se o Registro R será exportado |
| TipDcm | Number(004,0) | Sim | Tipo de Declaração ISS Municipal |
| CodDcm | Number(009,0) | Sim | Código da declaração |
| RegApu | Number(001,0) | Sim | Regime de Apuração do imposto |
| ModRel | String(012) | Sim | Modelo do Relatório |
| AprMun | String(001) | Sim | Apresentar Notas Emitidas no Mesmo Município do Tomador |
| VerDcm | String(030) | Sim | Versão da Declaração ISS Municipal |
| TrsEdc | String(001) | Sim | Transmitir NFTS para o e-docs |

---

## Chave Primária

- CodEmp
- CodRai
- DatIni

---

## Índices

### E008GDM_FKIndice1

**Tipo:** Não unico

Campos:
- CodRai

### E008GDM_FKIndice2

**Tipo:** Não unico

Campos:
- CodDec

### E008GDM_FKIndice3

**Tipo:** Não unico

Campos:
- CodDcm

---

## Relacionamentos

Nenhum relacionamento cadastrado.
