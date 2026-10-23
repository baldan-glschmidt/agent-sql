# R030CPT

## Descrição

eSocial JR - Processo Trabalhista

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| OriPro | Number(001,0) | Não | Origem do processo/demanda |
| ObsPro | String(999) | Sim | Observações relacionadas ao processo judicial ou à demanda submetida à CCP ou ao NINTER |
| DatSen | Date | Sim | Data da sentença ou da homologação do acordo do processo judicial |
| UfVara | String(002) | Sim | Unidade da Federação onde está localizada a Vara em que o processo tramitou |
| CodMun | Number(007,0) | Sim | Código do município, conforme tabela do IBGE |
| IdeVar | String(004) | Sim | Código de identificação da Vara em que o processo tramitou |
| DatCon | Date | Sim | Data da conciliação |
| CelAco | Number(001,0) | Sim | Âmbito de celebração do acordo |
| CnpjSi | Number(014,0) | Sim | CNPJ do sindicato representativo do trabalhador, no âmbito da CCP ou NINTER - Obsoleto |
| CfjSin | String(014) | Sim | CNPJ do sindicato representativo do trabalhador, no âmbito da CCP ou NINTER |

---

## Chave Primária

- NumEmp
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
